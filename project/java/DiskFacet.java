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
  A disk facet is a grouping of characteristics unique to a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DiskFacet extends Facet {

  private Integer diskSize;
  private String diskType;
  private Integer freeSpace;
  private List<ObservableObject> partition;


}