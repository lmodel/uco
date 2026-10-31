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
  A task action type is a grouping of characteristics for a scheduled action to be completed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaskActionType extends UcoInherentCharacterizationThing {

  private String actionID;
  private String actionType;
  private IComHandlerActionType iComHandlerAction;
  private ObservableObject iEmailAction;
  private IExecActionType iExecAction;
  private IShowMessageActionType iShowMessageAction;


}