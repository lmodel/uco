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
  An IShow message action type is a grouping of characteristics unique to an action that shows a message box when a task is activate. [based on https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-ishowmessageaction?redirectedfrom=MSDN]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IShowMessageActionType extends UcoInherentCharacterizationThing {

  private String showMessageBody;
  private String showMessageTitle;


}