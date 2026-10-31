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
  A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the intersection of specific latitude, longitude, and altitude values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LatLongCoordinatesFacet extends Facet {

  private BigDecimal altitude;
  private BigDecimal latitude;
  private BigDecimal longitude;


}