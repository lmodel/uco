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
  A symbolic link is a file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SymbolicLink extends FileSystemObject {



}