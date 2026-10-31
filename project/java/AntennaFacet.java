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
  An antenna alignment facet contains the metadata surrounding the cell tower's antenna position.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AntennaFacet extends Facet {

  private BigDecimal antennaHeight;
  private BigDecimal azimuth;
  private BigDecimal elevation;
  private BigDecimal horizontalBeamWidth;
  private BigDecimal signalStrength;
  private BigDecimal skew;


}