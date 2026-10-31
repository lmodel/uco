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
  A configuration is a grouping of characteristics unique to a set of parameters or initial settings for the use of a tool, application, software, or other cyber object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Configuration extends UcoObject {

  private List<ConfigurationEntry> configurationEntry;
  private List<Dependency> dependencies;
  private List<String> usageContextAssumptions;


}