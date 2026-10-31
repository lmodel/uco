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
  An application facet is a grouping of characteristics unique to a particular software program designed for end users.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ApplicationFacet extends Facet {

  private String applicationIdentifier;
  private List<ApplicationVersion> installedVersionHistory;
  private Integer numberOfLaunches;
  private String observableVersion;
  private ObservableObject operatingSystem;


}