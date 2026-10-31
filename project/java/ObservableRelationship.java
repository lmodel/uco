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
  An observable relationship is a grouping of characteristics unique to an assertion of an association between two observable objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ObservableRelationship extends Observable {

  private List<ZonedDateTime> endTime;
  private boolean isDirectional;
  private String kindOfRelationship;
  private List<UcoObject> source;
  private List<ZonedDateTime> startTime;
  private UcoObject target;


}