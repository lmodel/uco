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
  A Windows Task facet is a grouping of characteristics unique to a Windows Task (a process that is scheduled to execute on a Windows operating system by the Windows Task Scheduler). [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsTaskFacet extends Facet {

  private ObservableObject account;
  private String accountLogonType;
  private String accountRunLevel;
  private List<TaskActionType> actionList;
  private ObservableObject application;
  private Integer exitCode;
  private List<String> flags;
  private String imageName;
  private Integer maxRunTime;
  private ZonedDateTime mostRecentRunTime;
  private ZonedDateTime nextRunTime;
  private ZonedDateTime observableCreatedTime;
  private String parameters;
  private String priority;
  private String status;
  private String taskComment;
  private String taskCreator;
  private List<TriggerType> triggerList;
  private ObservableObject workItemData;
  private ObservableObject workingDirectory;


}