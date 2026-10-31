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
  A pipe is a mechanism for one-way inter-process communication using message passing where data written by one process is buffered by the operating system until it is read by the next process, and this uni-directional channel disappears when the processes are completed. [based on https://en.wikipedia.org/wiki/Pipeline_(Unix) ; https://en.wikipedia.org/wiki/Anonymous_pipe]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Pipe extends ObservableObject {



}