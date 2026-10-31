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
  An operating system facet is a grouping of characteristics unique to the software that manages computer hardware, software resources, and provides common services for computer programs. [based on https://en.wikipedia.org/wiki/Operating_system]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OperatingSystemFacet extends Facet {

  private List<String> advertisingID;
  private String bitness;
  private Dictionary environmentVariables;
  private ZonedDateTime installDate;
  private Boolean isLimitAdTrackingEnabled;
  private Identity manufacturer;
  private String observableVersion;


}