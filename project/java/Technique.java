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
  A technique is a class of actions joined by some common characteristics. The class uco-action:Technique is a metaclass. A Technique instance is an owl:Class that is a subclass of uco-action:Action.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Technique extends UcoType {

  private List<String> techniqueID;


}