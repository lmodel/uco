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
  A trigger type is a grouping of characterizes unique to a set of criteria that, when met, starts the execution of a task within a Windows operating system. [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TriggerType extends UcoInherentCharacterizationThing {

  private Boolean isEnabled;
  private ZonedDateTime triggerBeginTime;
  private String triggerDelay;
  private ZonedDateTime triggerEndTime;
  private String triggerFrequency;
  private String triggerMaxRunTime;
  private String triggerSessionChangeType;
  private String triggerType;


}