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
  A dictionary entry is a single (term/key, value) pair.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DictionaryEntry extends UcoInherentCharacterizationThing {

  private String key;
  private String typesValue;


}