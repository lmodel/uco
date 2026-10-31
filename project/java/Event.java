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
  An Event is a noteworthy occurrence (something that happens or might happen).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Event extends UcoObject {

  private List<ZonedDateTime> endTime;
  private List<Dictionary> eventAttribute;
  private List<UcoObject> eventContext;
  private List<String> eventType;
  private List<ZonedDateTime> startTime;


}