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
  An application version is a grouping of characteristics unique to a particular software program version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ApplicationVersion extends UcoInherentCharacterizationThing {

  private ZonedDateTime installDate;
  private String observableVersion;
  private ZonedDateTime uninstallDate;


}