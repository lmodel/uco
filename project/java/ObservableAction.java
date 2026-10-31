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
  An observable action is a grouping of characteristics unique to something that may be done or performed within the digital domain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ObservableAction extends Observable {

  private Integer actionCount;
  private String actionStatus;
  private ZonedDateTime actionEndTime;
  private List<UcoObject> actionObject;
  private ZonedDateTime actionStartTime;
  private UcoObject environment;
  private List<UcoObject> error;
  private List<UcoObject> instrument;
  private List<Location> location;
  private List<UcoObject> participant;
  private UcoObject performer;
  private List<UcoObject> result;
  private List<Action> subaction;


}