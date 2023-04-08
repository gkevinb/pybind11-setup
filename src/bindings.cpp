#include <pybind11/pybind11.h>
#include "simple.h"

namespace py = pybind11;

PYBIND11_MODULE(simple, m) {
    m.doc() = "pybind11 sound plugin";
    m.def("fibonacci", &fibonacci, "Calculate nth fibonacci number");
    m.def("leibniz_pi", &leibnizPi, "Calculate pi using Leibniz series");
}