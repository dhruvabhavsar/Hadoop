import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

public class InvertedIndex {

    public static class InvertedIndexMapper extends Mapper<LongWritable, Text, Text, Text> {

		private Text word = new Text();
		private Text documentID = new Text();

		@Override
		public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
			
			// Find document ID of the document that the input line belongs to
			documentID = new Text(((FileSplit) context.getInputSplit()).getPath().getName());

			// Conver the input line of text from Text type to String
			String line = value.toString();

			// Tokenize the input line of text
			StringTokenizer tokenizer = new StringTokenizer(line);
			
			// For each word in the line emit a key-valye record where 
			// the key is equal to the word and the value is equal to
			// the document ID
			while (tokenizer.hasMoreTokens()) {
				word.set(tokenizer.nextToken());
				context.write(word, documentID);
			}
		}
	}

	public static class InvertedIndexReducer extends Reducer<Text, Text, Text, Text> {

		@Override
		public void reduce(final Text key, final Iterable<Text> values,
				final Context context) throws IOException, InterruptedException {

			// Convert the list of document IDs (that is argument 'values') 
			// associated with the word (that is argument 'key') to a string
			// where postings are separted by " , "
			StringBuilder postings = new StringBuilder();
			for (Text value : values) {
				
				
				postings.append(value.toString());

				if (values.iterator().hasNext()) {
					postings.append(" , ");
				}
			}

			// Emit a key-value record where the key is the word
			// and value id the list of posting
			// (here we do not keep any payload data in inverted index)
			context.write(key, new Text(postings.toString()));
		}
	}

	public static void main(String[] args) throws Exception {

		Configuration conf = new Configuration();

		Job job = Job.getInstance(conf, "InvertedIndex");
		job.setJar("inverted.jar");
		job.setJarByClass(InvertedIndex.class);
    

		job.setMapperClass(InvertedIndexMapper.class);
		job.setReducerClass(InvertedIndexReducer.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}