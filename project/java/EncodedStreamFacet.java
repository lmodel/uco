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
  An encoded stream facet is a grouping of characteristics unique to the conversion of a body of data content from one form to another form.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EncodedStreamFacet extends Facet {

  private String encodingMethod;


}