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
  A dictionary is list of (term/key, value) pairs with each term/key having an expectation to exist no more than once. types:Dictionary alone does not validate this expectation, but validation is available. For use cases where this expectation must be validated, the subclass types:ProperDictionary should be used instead of types:Dictionary. For instances where this expectation has been found to be violated, the subclass types:ImproperDictionary should be used instead of types:Dictionary.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Dictionary extends UcoInherentCharacterizationThing {

  private List<DictionaryEntry> entry;


}