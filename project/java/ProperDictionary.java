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
  A proper dictionary is list of (term/key, value) pairs with each term/key existing no more than once.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProperDictionary extends Dictionary {



}