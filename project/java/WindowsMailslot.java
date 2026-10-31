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
  A Windows mailslot is is a pseudofile that resides in memory, and may be accessed using standard file functions. The data in a mailslot message can be in any form, but cannot be larger than 424 bytes when sent between computers. Unlike disk files, mailslots are temporary. When all handles to a mailslot are closed, the mailslot and all the data it contains are deleted. [based on https://docs.microsoft.com/en-us/windows/win32/ipc/about-mailslots]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsMailslot extends ObservableObject {



}