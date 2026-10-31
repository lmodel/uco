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
  An NTFS file facet is a grouping of characteristics unique to a file on an NTFS (new technology filesystem) file system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NTFSFileFacet extends Facet {

  private List<AlternateDataStream> alternateDataStreams;
  private Integer entryID;
  private String sid;


}