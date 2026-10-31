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
  A Windows volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single Windows file system. [based on https://en.wikipedia.org/wiki/Volume_(computing)]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsVolumeFacet extends Facet {

  private String driveLetter;
  private String driveType;
  private List<String> windowsVolumeAttributes;


}