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
  An archive file facet is a grouping of characteristics unique to a file that is composed of one or more computer files along with metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ArchiveFileFacet extends Facet {

  private String archiveType;
  private String comment;
  private String observableVersion;


}