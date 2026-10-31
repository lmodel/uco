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
  A character device node is a UNIX filesystem special file that serves as a conduit to communicate with devices, providing only a serial stream of input or accepting a serial stream of output. Character device nodes are used to apply access rights to the devices and to direct operations on the files to the appropriate device drivers. [based on https://en.wikipedia.org/wiki/Unix_file_types]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CharacterDeviceNode extends FileSystemObject {



}