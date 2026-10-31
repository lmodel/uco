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
  An event record is something that happens in a digital context (e.g., operating system events).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EventRecord extends ObservableObject {



}