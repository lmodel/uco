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
  A data range facet is a grouping of characteristics unique to a particular contiguous scope within a block of digital data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataRangeFacet extends Facet {

  private Integer rangeOffset;
  private String rangeOffsetType;
  private Integer rangeSize;


}