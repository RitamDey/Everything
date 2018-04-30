import java.io.BufferedWriter;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.File;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.nio.file.StandardOpenOption;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;


class Main {
	public static void main(String[] args) {
		String[] data = {
			"Line 1",
			"Line 2 2",
			"Line 3 3 3",
			"Line 4 4 4 4",
			"Line 5 5 5 5 5",
		};

		try(FileSystem zipFS = openZip(Paths.get("myData.zip"))) {
			copyToZip(zipFS);
		} catch(Exception e) {
			System.out.println(e.getClass().getSimpleName() + " - " + e.getMessage());
		}
	}

	public static FileSystem openZip(Path zipPath) throws IOException, URISyntaxException{
		Map<String, String> providedProps = new HashMap<>();
		providedProps.put("create", "true");

		// Fully qualified Path URI with type jar:file which represents
		// zip files in the Java system
		URI zipURI = new URI("jar:file", zipPath.toUri().getPath(), null);

		FileSystem zipFS = FileSystem.newFileSystem(zipURI, providedProps);

		return zipFS;
	}

	public static void copyToZip(FileSystem zipFS) throws IOException {

	}
}
