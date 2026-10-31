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
  A volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VolumeFacet extends Facet {

  private Integer sectorSize;
  private String volumeID;


}