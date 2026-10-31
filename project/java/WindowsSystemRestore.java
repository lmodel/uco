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
  A Windows system restore is a capture of a Windows computer's state (including system files, installed applications, Windows Registry, and system settings) at a particular point in time such that the computer can be reverted to that state in the event of system malfunctions or other problems. [based on https://en.wikipedia.org/wiki/System_Restore]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsSystemRestore extends ObservableObject {



}