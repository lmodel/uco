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
  A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such as the Global Positioning System (GPS).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GPSCoordinatesFacet extends Facet {

  private BigDecimal hdop;
  private BigDecimal pdop;
  private BigDecimal tdop;
  private BigDecimal vdop;


}