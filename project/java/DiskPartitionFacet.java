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
  A disk partition facet is a grouping of characteristics unique to a particular managed region on a storage mechanism.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DiskPartitionFacet extends Facet {

  private String diskPartitionType;
  private String mountPoint;
  private ZonedDateTime observableCreatedTime;
  private String partitionID;
  private Integer partitionLength;
  private Integer partitionOffset;
  private Integer spaceLeft;
  private Integer spaceUsed;
  private Integer totalSpace;


}