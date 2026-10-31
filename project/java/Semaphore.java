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
  A semaphore is a variable or abstract data type used to control access to a common resource by multiple processes and avoid critical section problems in a concurrent system such as a multitasking operating system. [based on https://en.wikipedia.org/wiki/Semaphore_(programming)]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Semaphore extends ObservableObject {



}