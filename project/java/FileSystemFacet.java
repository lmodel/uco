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
  A file system facet is a grouping of characteristics unique to the process that manages how and where data on a storage medium is stored, accessed and managed. [based on https://www.techopedia.com/definition/5510/file-system]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FileSystemFacet extends Facet {

  private Integer clusterSize;
  private String fileSystemType;


}