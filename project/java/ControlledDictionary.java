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
  A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is constrained to an explicitly defined set of values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlledDictionary extends Dictionary {



}