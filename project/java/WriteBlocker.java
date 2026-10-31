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
  A write blocker is a device that allows read-only access to storage mediums in order to preserve the integrity of the data being analyzed. Examples include Tableau, Cellibrite, Talon, etc.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WriteBlocker extends Device {



}