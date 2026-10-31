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
  An IExec action type is a grouping of characteristics unique to an action that executes a command-line operation on a Windows operating system. [based on https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-iexecaction?redirectedfrom=MSDN]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IExecActionType extends UcoInherentCharacterizationThing {

  private String execArguments;
  private List<Hash> execProgramHashes;
  private String execProgramPath;
  private String execWorkingDirectory;


}