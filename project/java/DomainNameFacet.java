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
  A domain name facet is a grouping of characteristics unique to an identification string that defines a realm of administrative autonomy, authority or control within the Internet. [based on https://en.wikipedia.org/wiki/Domain_name]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DomainNameFacet extends Facet {

  private Boolean isTLD;
  private String observableValue;


}