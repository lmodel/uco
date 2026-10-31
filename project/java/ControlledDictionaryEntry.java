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
  A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an explicitly defined set of values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlledDictionaryEntry extends DictionaryEntry {



}