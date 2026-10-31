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
  A Windows service facet is a grouping of characteristics unique to a specific Windows service (a computer program that operates in the background of a Windows operating system, similar to the way a UNIX daemon runs on UNIX). [based on https://en.wikipedia.org/wiki/Windows_service]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsServiceFacet extends Facet {

  private List<String> descriptions;
  private String displayName;
  private String groupName;
  private String serviceName;
  private String serviceStatus;
  private String serviceType;
  private String startCommandLine;
  private String startType;


}