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
  A compressed stream facet is a grouping of characteristics unique to the application of a size-reduction process to a body of data content.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompressedStreamFacet extends Facet {

  private String compressionMethod;
  private BigDecimal compressionRatio;


}