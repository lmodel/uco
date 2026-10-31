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
  A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative address.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SimpleAddressFacet extends Facet {

  private String addressType;
  private String country;
  private String locality;
  private String postalCode;
  private String region;
  private String street;


}