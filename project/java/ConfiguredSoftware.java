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
  A ConfiguredSoftware is a Software that is known to be configured to run in a more specified manner than some unconfigured or less-configured Software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConfiguredSoftware extends Software {

  private Software isConfigurationOf;
  private Configuration usesConfiguration;


}