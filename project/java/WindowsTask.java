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
  A Windows task is a process that is scheduled to execute on a Windows operating system by the Windows Task Scheduler. [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsTask extends ObservableObject {



}