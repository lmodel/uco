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
  A user session is a temporary and interactive information interchange between two or more communicating devices within the managed scope of a single user. [based on https://en.wikipedia.org/wiki/Session_(computer_science)]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class UserSession extends ObservableObject {



}