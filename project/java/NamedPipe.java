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
  A named pipe is a mechanism for FIFO (first-in-first-out) inter-process communication. It is persisted as a filesystem object (that can be deleted like any other file), can be written to or read from by any process and exists beyond the lifespan of any process interacting with it (unlike simple anonymous pipes). [based on https://en.wikipedia.org/wiki/Named_pipe]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamedPipe extends FileSystemObject {



}