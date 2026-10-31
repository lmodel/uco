package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A file facet is a grouping of characteristics unique to the storage of a file (computer resource for recording data discretely in a computer storage device) on a file system (process that manages how and where data on a storage device is stored, accessed and managed). [based on https://en.wikipedia.org/Computer_file and https://www.techopedia.com/definition/5510/file-system]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FileFacet extends Facet {

  private ZonedDateTime accessedTime;
  private String allocationStatus;
  private String extension;
  private List<String> fileName;
  private List<String> filePath;
  private List<Boolean> isDirectory;
  private ZonedDateTime metadataChangeTime;
  private ZonedDateTime observableCreatedTime;
  private ZonedDateTime observableModifiedTime;
  private Integer sizeInBytes;


}