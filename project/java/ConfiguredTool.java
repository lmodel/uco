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
  A ConfiguredTool is a Tool that is known to be configured to run in a more specified manner than some unconfigured or less-configured Tool.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConfiguredTool extends Tool {

  private Tool isConfigurationOf;
  private Configuration usesConfiguration;


}