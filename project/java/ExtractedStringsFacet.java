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
  An extracted strings facet is a grouping of characteristics unique to one or more sequences of characters pulled from an observable object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExtractedStringsFacet extends Facet {

  private List<ExtractedString> strings;


}