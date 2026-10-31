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
  A simple name facet is a grouping of characteristics unique to the personal name (e.g., Dr. John Smith Jr.) held by an identity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SimpleNameFacet extends IdentityFacet {

  private List<String> familyName;
  private List<String> givenName;
  private List<String> honorificPrefix;
  private List<String> honorificSuffix;


}